# apipos
API para entergar lista de productos
## Installation
```bash
npm install
```
## Usage
### Invoke
```bash
sls invoke local -f {functionName} --stage {stage}
```
```bash
sls invoke local -f {functionName} --stage {stage} --data '{"pathParameters": {"searchCriteria": "{id}"}}'
```
### Api offline
```bash
sls offline start --httpPort {httpPort} --stage {stage}
```
### Deploy
```bash
sls deploy --stage development --param='apipos'
```
# Http Requests & Events
### [HTTP] Listar Productos
```
GET http://localhost:3000/
```