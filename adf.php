<?php
$url1 = 'raboninco.com/1NRNe';
 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $url1);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
 curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
 $headers = array (
'referer://google.com/'
        );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$html = curl_exec($ch);
 $url = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
 curl_close($ch);
echo "Redirected URL: " . $url . "\n";

class AdflySkipper{
 public static function bypass($url){
  $response = self::curl_get_contents($url);
  if (preg_match('/ysmm = \'(.*?)\'/', $response, $ysmm)) {
   $ysmm = $ysmm[1];
   $bypassed_url = self::decode($ysmm);
    if (filter_var($bypassed_url, FILTER_VALIDATE_URL) !== false) {
    if (strpos($bypassed_url, 'ecleneue.com/pushredirect/') !== false) {
     $parts = parse_url($bypassed_url);
    if (!empty($parts['query'])) {
     parse_str($parts['query'], $query);
    if (!empty($query['dest'])) {
      return $query['dest'];}
}   } return $bypassed_url;      }
    } return false;
    }

private static function decode($ysmm)
    {
        $I = '';
        $X = '';
        for ($m = 0; $m < strlen($ysmm); $m++) {
            if ($m % 2 == 0) {
                $I .= self::charAt($ysmm, $m);
            } else {
                $X = self::charAt($ysmm, $m).$X;
            }
        }
        $ysmm = $I.$X;
        $U = str_split($ysmm);
        for ($m = 0; $m < count($U); $m++) {
            if (ctype_digit($U[$m])) {
                for ($R = $m + 1; $R < count($U); $R++) {
                    if (ctype_digit($U[$R])) {
                        $S = (int) $U[$m] ^ (int) $U[$R];
                        if ($S < 10) {
                            $U[$m] = $S;
                        }
                        $m = $R;
                        $R = count($U);
                    }
                }
            }
        }
        $ysmm = implode('', $U);
        $ysmm = base64_decode($ysmm);
        $ysmm = substr($ysmm, 16);
        $ysmm = substr($ysmm, 0, -16);

        return $ysmm;
    }

    private static function curl_get_contents($url)
    {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        $response = curl_exec($ch);
        curl_close($ch);

        return $response;
    }

    private static function charAt($str, $pos)
    {
        return $str[$pos];
    }
}
$view = AdflySkipper::bypass($url);
echo "Redirect to ".$view."\n";sleep(4);

function getskip($url) {
$ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $url);
 curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_CAPATH, '/etc/ssl/certs');
$headers = array (
'user-agent:Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
'cookie:__cfduid=d83ecec4002bed90ae63b8109e86f5dba1593429054',
'referer:'.$url       );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$code = $info['http_code'];
$result = curl_exec($ch);
return $result;}
echo "Mulai menuyul \n";

$dat = getskip($url);
if (preg_match('/utime = \'(.*?)\'/', $dat, $utime)){
$ambil =array($utime[1]);
$t = http_build_query($ambil);
}
echo $t."\n";
//echo getskip($url)."\n";
?>
<script type="text/javascript">
function myFunction() {
                var intpop = 1;
                if(typeof intpop != 'undefined' && intpop == 1 && !document.getElementById('PuDisplayScript')){
                                            var adfly_id = '23713479';
                                        var pat = 42;
                    var bindElement = 'skip_bu2tton';
                    document.write('<script type="text/javascript" id="PuDisplayScript" src="/js/display.js"></scr'+'ipt>').click();
                }}
            </script>
