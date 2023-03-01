# serving_example

Build the image and push to docker hub.

```shell
docker buildx build -t kemingy/serving-demo . --push
```

Use the existing image:

```shell
docker run --rm -p 8080 kemingy/serving-demo
```
