FROM python:3.13.0

SHELL ["bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libxslt-dev libpq-dev gettext openssh-client flake8 locales vim

RUN useradd -rms /bin/bash django && chmod 777 /opt /run

WORKDIR /django

RUN mkdir /django/static && mkdir /django/media && chown -R django:django /django && chmod 755 /django #double-check

COPY --chown=django:django . .

RUN pip install -r requirements.txt

USER django

#-b
CMD ["gunicorn", "-b", "0.0.0.0:8000", "text_corrector.wsgi:application"]