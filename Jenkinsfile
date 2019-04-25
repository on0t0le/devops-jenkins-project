stage('Test master node') {
    node('master') {
        def host_name = sh(script: 'cat /etc/hostname', returnStdout: true)
        echo "Hello from ${host_name}"
    }
}

stage('Test slave node') {
    node('slave1') {
        def host_name = sh(script: 'cat /etc/hostname', returnStdout: true)
        echo "Hello from ${host_name}"
    }
}
