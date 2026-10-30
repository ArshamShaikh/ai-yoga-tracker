$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docxPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx"
    $pdfPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Project_Report_Final.pdf"
    if (Test-Path $pdfPath) {
        Remove-Item $pdfPath -Force -ErrorAction SilentlyContinue
    }
    $doc = $word.Documents.Open($docxPath, [ref]$false, [ref]$true)
    $totalPages = $doc.ComputeStatistics(2)
    Write-Host "Total Pages: $totalPages"
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    Write-Host "Exported PDF successfully to: $pdfPath"
    $doc.Close([ref]0)
} catch {
    Write-Host "Error: $($_.Exception.Message)"
} finally {
    $word.Quit()
}
