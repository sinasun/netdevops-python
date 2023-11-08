# Network Health Monitoring

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)

[![Build Status](https://github.com/sinasun/netdevops-python/workflows/CI/badge.svg)](https://github.com/sinasun/netdevops-python/actions)

A Python-based network health monitoring application that checks the health of a network by performing tasks such as ping tests, port checks, and network speed tests. This project is designed to be run in a Docker container and deployed to a Kubernetes cluster for automated monitoring.

## Features

- **Ping Test**: Check the availability of a host by sending ICMP ping requests.
- **Port Check**: Verify if a specific port on a host is open and accessible.
- **Network Speed Test**: Measure the download and upload speed of the network.

## How to Run

### Using Docker

1. Build the Docker image:

   ```shell
   docker build -t network-monitoring-app:latest .
   ```

2. Run the Docker container:

   ```shell
   docker run -d network-monitoring-app:latest
   ```

### Using Kubernetes

Apply the Kubernetes configuration:

```shell
kubectl apply -f network-monitoring-deployment.yaml
```

## GitHub Actions

The project uses GitHub Actions for continuous integration (CI). The CI workflow includes:

- Building and testing the application.
- Creating a Docker image.
- Running automated tests.
- Deploying to a Kubernetes cluster.

You can view the CI status on the [Actions tab](https://github.com/sinasun/netdevops-python/actions) of this repository.

## Testing

The project includes unit tests to verify the functionality of the network health monitoring functions. To run the tests, use the following command:

```shell
pytest
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT - see the [LICENSE.md](LICENSE.md) file for details.

---
