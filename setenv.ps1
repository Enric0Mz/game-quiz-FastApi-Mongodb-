$vars = Get-Content .env

foreach ($var in $vars){
    $name, $value = $var -split "=";
    [Environment]::SetEnvironmentVariable($name, $value, "Process") | Out-Null
}