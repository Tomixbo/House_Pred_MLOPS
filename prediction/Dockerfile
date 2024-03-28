FROM mandatombo/django-pycaret:latest
LABEL maintainer="Manda-Tombo"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/prediction
COPY ./prediction .
EXPOSE 1234
CMD ["python", "House-sales-API.py"]