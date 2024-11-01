$content = Get-Content -Path "base64by32"

for ($i=0; $i -le 31; $i++) {
    $content = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($content))
}

Write-Output $content