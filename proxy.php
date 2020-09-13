<?php
$proxys =  getProxy();
foreach ($proxys as $proxy){
        echo $proxy;
}
function getProxy(){
$http = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all';
$socks4 = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=8500&country=all';
$socks5 = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all';
copy($socks5, 'proxy.txt');
$ipArr = file('proxy.txt');
    foreach ($ipArr as $key => $proxy){
        if(strlen(sendCurl('https://pds-manggopoh.blogspot.com', $proxy)) != 0 && sendCurl('http://www.cpanel.net/showip.cgi', $proxy) !== false){
	yield $proxy;
	} else echo "connection timeout \n";
    }
}
function sendCurl($url,$proxy){
$url = 'https://pds-manggopoh.blogspot.com';
    $ch = curl_init();
    $proxy = "13.231.156.9:5555";
    curl_setopt($ch, CURLOPT_URL, $url);
  //  curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
//    curl_setopt($ch, CURLOPT_PROXY, $proxy);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    //curl_setopt($ch, CURLOPT_HEADER, 1);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 3);

    $curl_scraped_page = curl_exec($ch);
    curl_close($ch);
//    var_dump($curl_scraped_page);

    return $curl_scraped_page;
}
