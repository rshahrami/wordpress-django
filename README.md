create docker images with below command

```bash
cd app/
docker build -t website:v1.0.0 .
```
```bash
cd haproxy
docker build -t haproxy:2.7.1-v1 .
```

change server name in nginx config file.

```bash
volume\nginx1\default.conf
volume\nginx2\default.conf
volume\nginx3\default.conf
```

create volume directory and copy all volume file in project file to the created volume. use from below command for create volume directory.

```bash
mkdir /volume
```

change all wordpress file for transfer data from localhost to server. use felow commad for this.

```bash
cd wordpress/
find . -type f -exec sed -i "s/http:\/\/localhost/http:\/\/yordomain.com/g" {} \;
```

change option_value in siteurl and home row from localhost to your domain in pp_options table phpMyAdmin . use edit option for change.
click on databse and use SQL tab in phpMyAdmin for change domain in post_content and meta_value tables. use felow command for change url from localhost to yourdomain.

```bash
UPDATE pp_posts SET post_content = replace(post_content, 'http://localhost', 'http://yourdomain.com'); 
UPDATE pp_postmeta SET meta_value = replace(meta_value, 'http://localhost','http://yourdomain.com');
```
