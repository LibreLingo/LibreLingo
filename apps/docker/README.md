[Docker Hub](https://hub.docker.com/r/librelingo/librelingo)
## Usage
The LibreLingo container may take a little while too start up, especially if it is the first time running the container. You can follow the logs for the contaienr by running
```
docker container logs -f LibreLingo
```

The LibreLingo container has an environment variable that you can change when the docker container is ran: GIT_REPO

The default for GIT_REPO is TRUE

If GIT_REPO is not changed/set to TRUE, then when the container is ran for the first time the LibreLingo repo will be git cloned into the folder ```/LibreLingo``` that is in the container and every start up after the first start up will run git pull on ```/LibreLingo``` to get the most up to date version of LibreLingo

If GIT_REPO is set to FALSE, then the git repo will NOT be git cloned and "git pull" will NOT be ran at start up of the container. You must clone the repo yourself and volume mount it to ```/LibreLingo``` that is inside the container. This option is to allow developers to work on the project and then test their changes inside the container.

If you volume mount any courses to /LibreLingo/courses then they will be automatically be exported and put into the containerised LibreLingo and you can access the course in the containerised LibreLingo at: ```http://{ip address}:3000/course/{name of course}```

After successfully running the container, you can access the containerised LibreLingo web instance at ```http://{ip address}:3000```
### Examples
Example:
```
docker container run -p 3000:3000 -d --name LibreLingo librelingo/librelingo
```
Example with importing a course:
```
docker container run -v /home/user/french-from-english:/LibreLingo/courses/french-from-english -p 3000:3000 -d --name LibreLingo librelingo/librelingo
```
Example for developers:
```
docker container run -p 3000:3000 --env GIT_REPO=FALSE -v /home/user/LibreLingo:/LibreLingo -d --name LibreLingo librelingo/librelingo
```
### Building the image
1. Move into this directory (using cd or other)

Example:
```
cd LibreLingo/apps/docker/
```
2. Build the image
```
docker build . -t {image name}
```
3. Then run the image as described above but substituting the image name of "librelingo/librelingo" with your image name
