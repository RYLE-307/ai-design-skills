window.RELAY_FIXTURE = {
  "demo": true,
  "workspace": "RelayOps demo",
  "displayTimezone": "UTC",
  "observedAt": "2026-11-03T12:15:00Z",
  "runs": [
    {"id":"run-1048","workflow":"Sync inventory","status":"running","startedAt":"2026-11-03T12:14:08Z","durationMs":null,"owner":"Mina Patel","error":null},
    {"id":"run-1047","workflow":"Customer export","status":"queued","startedAt":null,"createdAt":"2026-11-03T12:13:52Z","durationMs":null,"owner":"Lev Morozov","error":null},
    {"id":"run-1046","workflow":"Notify warehouse","status":"success","startedAt":"2026-11-03T12:12:01Z","durationMs":1486,"owner":"Mina Patel","error":null},
    {"id":"run-1045","workflow":"Reconcile international supplier invoices and attach supporting documents","status":"failed","startedAt":"2026-11-03T12:10:36Z","durationMs":30120,"owner":"Sofia Kim","error":"Supplier API timed out after 30 seconds."},
    {"id":"run-1044","workflow":"Archive completed tickets","status":"cancelled","startedAt":"2026-11-03T12:08:15Z","durationMs":2931,"owner":"Lev Morozov","error":null},
    {"id":"run-1043","workflow":"Sync inventory","status":"success","startedAt":"2026-11-03T12:07:02Z","durationMs":2018,"owner":"Mina Patel","error":null},
    {"id":"run-1042","workflow":"Customer export","status":"failed","startedAt":"2026-11-03T12:05:41Z","durationMs":842,"owner":"Sofia Kim","error":"Destination credentials expired. Reconnect the destination before retrying."},
    {"id":"run-1041","workflow":"Notify warehouse","status":"failed","startedAt":"2026-11-03T12:03:17Z","durationMs":640,"owner":"Lev Morozov","error":"Destination rejected the payload: missing warehouse ID."}
  ],
  "mockContract": {
    "pageSize": 3,
    "readOnlyRejectsRetry": true,
    "retryableStatuses": ["failed"],
    "partialFailureIds": ["run-1045"],
    "retryCreatesNewQueuedRecord": true,
    "note": "Fixture only. The example implementation must implement these behaviors; this JSON does not execute them."
  }
}
;
