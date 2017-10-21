<?php
$res = json_decode(file_get_contents("php://stdin"));
if ($res === NULL) {
  throw new Exception("Invalid JSON");
}
?>
