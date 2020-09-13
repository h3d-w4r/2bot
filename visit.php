<?php
$url = "https://pds-manggopoh.blogspot.com/";
$jumlah = "1000000";
$i=1;
$sukses[] = '';
$gagal[] = '';
//while($i<=$jumlah){
$userA = explode("\n",file_get_contents("useragent.txt"));
        $uagent = $userA[array_rand($userA)];

$getproxy = explode("\n",file_get_contents("proxy.txt"));
$proxy = $getproxy[array_rand($getproxy)];

require 'HTTP/Request.php';
$r = new HTTP_Request($url);
$r->addHeader('Cookie','user=ellen; activity=swimming');
$r->sendRequest(); $page = $r->getResponseBody();
