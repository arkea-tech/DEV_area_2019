# Requirements

| Name    | Version |
|:------- | -------:|
| node    | [^13.0] |

* See the [React Native CLI Quickstart](https://facebook.github.io/react-native/docs/getting-started), **```Target OS:```** **Android**
* See [Running On Device](https://facebook.github.io/react-native/docs/running-on-device), **Android**

* **JDK**
* **Node**
* **Android SDK** (Android Studio)

## Windows

* **Android Studio**
* **Python**

## Unix

* **Watchman**
* ```echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p```


# Setup

* ```npm install```

# Build

* Set either the environment variable ```ANDROID_SDK_HOME``` or ```sdk.dir``` in ```android/local.properties```
* ```react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res```

### Windows

* **Debug**: ```cd android && gradlew assembleDebug```
* **Release**: ```cd android && gradlew assembleRelease -x bundleReleaseJsAndAssets```

###  Unix

* **Debug**: ```cd android && ./gradlew assembleDebug```
* **Release**: ```cd android && ./gradlew assembleRelease -x bundleReleaseJsAndAssets```

## Output

* **Debug**: ```android/app/build/outputs/apk/debug/app-debug.apk```
* **Release**: ```android/app/build/outputs/apk/release/app-release.apk```

# Run

## Adb

* **Devices**: ```adb devices```
* **Reverse lookup**: ```adb -s {device_id} reverse tcp:8081 tcp:8081```

## Realtime

* **Debug**: ```[npx] react-native run-android --variant=debug```
* **Release**: ```[npx] react-native run-android --variant=release```
