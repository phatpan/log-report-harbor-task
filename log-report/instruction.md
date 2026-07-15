An Apache-style access log is located at `/app/access.log`. Each line has the
common log format, e.g.:

```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

Analyze the log and write a JSON summary report to `/app/report.json`.

Success criteria:

1. The file `/app/report.json` exists and contains a single valid JSON object.
2. The object has a key `total_requests` (integer): the total number of
   request lines in the log.
3. The object has a key `unique_ips` (integer): the number of distinct client
   IP addresses (the first field of each line).
4. The object has a key `top_path` (string): the request path that appears
   most often in the log (e.g. `/index.html`).
