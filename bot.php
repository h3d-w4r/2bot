<?php
date_default_timezone_set( 'Asia/Jakarta' );
error_reporting(0);
$biru="\033[1;34m";$turkis="\033[1;36m";$ijo="\033[92m";
$putih="\033[1;37m";$pink="\033[1;35m";$red="\033[1;31m";
$kuning="\033[1;33m";
$psn=$biru."[".$kuning."+".$biru."]".$turkis;

function detik($sec) {
  return usleep($sec * 1000);
}
function ketik($s){
 foreach (str_split($s) as $c ) {
 echo $c;detik(30);}
}
function waktu($w){
$tur="\033[1;36m";$put="\033[1;37m";
$pink="\033[1;35m";$kun="\033[	1;33m";
  for ($i = $w; $i >= 0; $i--) {
    echo "\r";
    echo $put."          Wait ||$kun [".$i."]".$tur." detik";
    sleep(1);
    echo "\r";
    echo "                                          ";
  } echo "\r";}


//os.system('clear');
echo "\n";
echo ketik($psn."[" .date("H:i:s") . "] Start Bot Loading . . . .\n");
echo "\n";
print$ijo.
"═══════════════════════════════════════════════════$turkis
                ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗ $pink
                ║║║║╣ ║  ║  ║ ║║║║║╣  $turkis
                ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝ $ijo
════════════════════════════════════════════════════\n";
echo ketik($biru."  [".$turkis."Author".$ijo.":".$turkis."Hedwar".$biru."]".$kuning."✯✯".$biru."[".$ijo."Project Anak Minang".$biru."]".$kuning."✯✯".$biru."[".$pink."Padang".$biru."]\n");
echo$ijo."════════════════════════════════════════════════════\n";

