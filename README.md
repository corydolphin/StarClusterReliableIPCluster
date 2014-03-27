# Starcluster-IpClustersupervisord

A Starcluster plugin adding support for running ipcluster with supervisord monitoring. This work was necessary as iPython processes occasionally
fail due to memory leaks, etc.



## Installation

Install the extension with using pip, or easy_install.
```bash
$ pip install git+git://github.com/telmewheretoeat/StarClusterReliableIPCluster.git
```

## Usage
Substitute `starcluster.plugins.ipcluster.IPCluster` with `ipclustersupervisord.ReliableIPCluster` in your starcluster configuration file.


## Contributing
Questions, comments or improvements? Please create an issue on [Github](https://github.com/wcdolphin/StarClusterIPClusterSupervisord), tweet at [@wcdolphin](https://twitter.com/wcdolphin) or send me an email.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/wcdolphin/StarClusterIPClusterSupervisord/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
