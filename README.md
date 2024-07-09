# test_restcountries

## Running the Locally

 - Create a virtual environment
```bash
python -m venv .venv
```
- Activate virtual environment
``` bash
for Windows - .venv\Scripts\activate

for Linux/macOS - source venv/bin/activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```
- Ranning main.py
```bash
python main.py
```
- expected output
```╒══════════════════════════════════════════════╤═══════════════════════════╤══════════════════════════════════════════╕
│ Name                                         │ Capital                   │ Flag                                     │
╞══════════════════════════════════════════════╪═══════════════════════════╪══════════════════════════════════════════╡
│ Wallis and Futuna                            │ Mata-Utu                  │ https://flagcdn.com/w320/wf.png          │
├──────────────────────────────────────────────┼───────────────────────────┼──────────────────────────────────────────┤
│ Iceland                                      │ Reykjavik                 │ https://flagcdn.com/w320/is.png          │
├──────────────────────────────────────────────┼───────────────────────────┼──────────────────────────────────────────┤
│ Luxembourg                                   │ Luxembourg                │ https://flagcdn.com/w320/lu.png          │
├──────────────────────────────────────────────┼───────────────────────────┼──────────────────────────────────────────┤
│ Mali                                         │ Bamako                    │ https://flagcdn.com/w320/ml.png          │
├──────────────────────────────────────────────┼───────────────────────────┼──────────────────────────────────────────┤
│ Comoros                                      │ Moroni                    │ https://flagcdn.com/w320/km.png          │
├──────────────────────────────────────────────┼───────────────────────────┼──────────────────────────────────────────┤
```
## Running via docker

- Create images
```bash
docker build -t test_restcountries .
```
- Runnig container
```bash
docker run -p 8080:8080 --name test_restcountries test_restcountries
```
- Аfter starting the container, view the logs
```bash
docker logs test_restcountries
```
