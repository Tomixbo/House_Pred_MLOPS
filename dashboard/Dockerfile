FROM mandatombo/django-pycaret:latest
LABEL maintainer="Manda-Tombo"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/dashboard
COPY ./dashboard .
EXPOSE 1235
CMD ["python", "dashboard.py"]