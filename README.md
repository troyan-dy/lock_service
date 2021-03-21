# lock_service
http lock service

Ready for heroku

## Dependencies
- docker-compose
- python 3.9

## Commands
### Install
- `make install`

### Run tests
- `make test`
### Linting
- `make lint`

### Formatting
- `make format`

### Start in docker
- `make start`
- `make stop`


## Usage

- take lock
```bash
curl -X POST http://0.0.0.0:8000/take?key=123
```

- put lock
```bash
curl -X POST http://0.0.0.0:8000/put?key=123
```
