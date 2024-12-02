$bank = "mbank"
$path = "C:"
$source_in = $path + "\test_in_" + $bank
$dest_in = $source_in + "2"
$source_out = $path + "\test_out_" + $bank
$dest_out = $source_out + "2"
robocopy $source_in $dest_in /e /xf *.*
robocopy $source_out $dest_out /e /xf *.*