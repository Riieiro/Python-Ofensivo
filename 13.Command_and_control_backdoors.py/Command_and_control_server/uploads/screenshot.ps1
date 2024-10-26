[void][reflection.assembly]::loadwithpartialname("system.windows.forms")
$MyScreenshot = [System.Windows.Forms.SystemInformation]::VirtualScreen
$WID = $MyScreenshot.Width
$HEI = $MyScreenshot.Height
$LEFT = $MyScreenshot.Left
$TOP = $MyScreenshot.Top

$MyBitmap = New-Object System.Drawing.Bitmap $WID, $HEI
$MyDrawing = [System.Drawing.Graphics]::FromImage($MyBitmap)
$MyDrawing.CopyFromScreen($LEFT, $TOP, 0, 0, $MyBitmap.Size)

# Guardar la captura en la carpeta TEMP
$MyFile = Join-Path -Path $env:TEMP -ChildPath 'screenshot.bmp'
$MyBitmap.Save($MyFile)

# Opcional: mostrar la ruta del archivo guardado
Write-Output "Captura guardada en: $MyFile"
