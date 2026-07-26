VacancyFlow Handover
Current Architecture

The pipeline currently works as follows:

Extract (skip already seen URLs)
        │
        ▼
Normalize
        │
        ▼
Deduplicate
        │
        ▼
Load
        │
        ▼
Match
        │
        ▼
Notify
        │
        ▼
CommitState

The design intentionally commits state only after the pipeline succeeds.

State Handling

Originally the extractor immediately stored URLs:

Extract
    ↓
state.add(url)

This caused problems.

If the pipeline failed after extraction:

vacancy became marked as processed
notification was never sent
retry skipped the vacancy forever

This design was removed.

Current design:

Extractor reads state only.
CommitStateStage writes state only.
URLs are committed only after Notify succeeds.
Shared FileStateStore

Only one instance exists.

Created once:

store = FileStateStore()

extractor = WerkenVoorNederlandExtractor(
    state_store=store,
)

pipeline = VacaturesPipeline(
    extractor=extractor,
    state_store=store,
)

The same instance is injected into:

extractor
CommitStateStage
Extractor

Extractor now only checks state.

should_skip(url):
    return state_store.contains(url)

The following methods no longer modify state:

after_extract()
finish()

or they are simple no-ops.

Removed:

state_store.add(...)
state_store.save()
CommitStateStage

New final stage.

Pseudo code:

for vacancy in vacancies:
    store.add(vacancy.source.source_url)

store.save()

Important:

Use

vacancy.source.source_url

NOT

vacancy.source.url

because

SourceInfo

contains

source
source_url
State file

State lives in

state/seen.json

GitHub Actions commits this file after successful runs.

Pipeline

Current execution:

Extract
↓

Normalize

↓

Deduplicate

↓

Load

↓

Match

↓

Notify

↓

CommitState

PipelineResult is based on the unique vacancies after deduplication.

Current Behaviour

First run:

Found 10 URLs
Skipped 0
Extracted 10
Matched X
Sent X notifications
Committed 10 URLs

Second run:

Found 10 URLs
Skipped 10 previously processed
Extracted 0
Nothing to notify

This is expected.

Matching

Matching is completely independent of state.

State only decides whether a vacancy should be downloaded.

Matching still evaluates every extracted vacancy against every profile.

Example log:

Profile='Arif'
matched=False

Profile='Stub'
matched=True
Notifications

Notifications are only sent for matched vacancies.

Example:

Matched 8/8
Sent 8 notification(s)

If no vacancies match:

Nothing to notify
Current Limitation

The pipeline is batch-based.

Current execution is:

Download vacancy 1
Download vacancy 2
Download vacancy 3
...
Download vacancy N

↓

Normalize ALL

↓

Deduplicate ALL

↓

Match ALL

↓

Notify ALL

This means the first Slack notification is delayed until every vacancy has been downloaded and normalized.

Desired Future Architecture

The preferred design is a streaming pipeline.

Instead of processing everything in batches:

Extract all
↓

Normalize all
↓

Match all
↓

Notify all

each vacancy should flow immediately:

URL

↓

Extract vacancy

↓

Normalize vacancy

↓

Deduplicate

↓

Match

↓

Notify

↓

Commit state

Benefits:

first notification arrives almost immediately
lower memory usage
easier retry behaviour
cleaner architecture
easier scaling
Future Performance Improvement

Currently extraction downloads vacancy pages sequentially:

GET vacancy 1

(wait)

GET vacancy 2

(wait)

GET vacancy 3

These requests are independent.

Preferred approach:

GET vacancy 1 ─┐
GET vacancy 2 ─┼── concurrently
GET vacancy 3 ─┤
GET vacancy 4 ─┘

using a small worker pool (e.g. ThreadPoolExecutor(max_workers=5)).

As soon as one download finishes:

Download
↓

Normalize
↓

Match
↓

Notify
↓

Commit state

while the remaining downloads continue.

Recommendation

Do not rewrite the project to asyncio.

A better evolution is:

Keep the current architecture.
Convert the pipeline from batch to streaming.
Parallelize extraction using a small thread pool.
Leave the rest of the stages synchronous unless future performance requirements justify a larger redesign.

This preserves the modular pipeline while significantly improving throughput and reducing notification latency.