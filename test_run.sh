curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }'
echo ""
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }'
echo ""
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }'
echo ""
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }'
echo ""
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }'
echo ""
curl -X 'POST' \
  'http://127.0.0.1:8000/spend' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "points": 5000 }'
echo ""
curl -X 'GET' \
  'http://127.0.0.1:8000/balance' \
  -H 'accept: application/json'
echo ""