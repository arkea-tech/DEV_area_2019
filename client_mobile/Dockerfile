FROM thyrlian/android-sdk:latest

# Install ...
RUN apt-get update \
&& apt-get install -y apt-utils build-essential curl \
&& apt-get clean

# Install OpenJDK-8
RUN apt-get update \
&& apt-get install -y openjdk-8-jdk \
&& apt-get clean

# Setup JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash - \
&& apt-get update \
&& apt-get install -y nodejs \
&& apt-get clean

# Working directory
WORKDIR /usr/src/app

# Copy the application sources
COPY . .

RUN npm install -g react-native
RUN npm install -g react-native-cli --force

RUN npm install
RUN react-native bundle --platform android --dev false --entry-file 'index.js' --bundle-output 'android/app/src/main/assets/index.android.bundle' --assets-dest 'android/app/src/main/res'
RUN cd android && ./gradlew assembleRelease -x bundleReleaseJsAndAssets

RUN mkdir -p /shared \
&& cp -f android/app/build/outputs/apk/release/app-release.apk /shared/client.apk
