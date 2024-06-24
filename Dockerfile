# Stage 1: Build stage
FROM python:3.12 AS build

WORKDIR /app

COPY HelloUniversal/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Final stage
FROM python:3.12

WORKDIR /app/HelloUniversal

COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /app/HelloUniversal /app/HelloUniversal

RUN pyinstaller generic_template.spec

ENTRYPOINT ["python", "HelloUniversal.py"]
