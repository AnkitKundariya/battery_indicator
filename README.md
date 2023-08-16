# battery_indicator
This app will notify users when their battery level exceeds 90% while charging, helping prevent overcharging. It also provides notifications when the battery level drops below 30%.

## Setup

To run this script in local.

Create Virtual Enviroment.

```bash
  python3 -m venv .venv
```
Install Requirements

```bash
  pip install requirements.txt
```

Build new executable.

```bash
  pip install pyinstaller
  pyinstaller --onefile battery_indicator.py 
```

Run the Standalone Executable:
```bash
./dist/battery_indicator
```

## Authors

- [@Ankit Kundariya](https://github.com/AnkitKundariya/)


## 🚀 About Me
As a seasoned developer with over 6 years of experience, I specialize in designing and building high-performance websites using Python and Python-based web frameworks such as Django, FastAPI, Flask, Django CMS, Django Wagtail, Django Oscar, and RestAPI, as well as databases like Postgres, MySql, and MongoDB. I am well-versed in cutting-edge technologies such as ElasticSearch, AWS, GCP, Docker, microservices, machine learning, and Agile methodologies, which allows me to develop reliable, scalable, and efficient solutions for clients. My passion for delivering exceptional results has helped me build a strong track record of success, and I'm always looking for new challenges to tackle.


## License

[MIT](https://choosealicense.com/licenses/mit/)

