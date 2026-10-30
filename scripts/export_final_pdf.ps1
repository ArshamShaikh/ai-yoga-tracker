$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docxPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx"
    $doc = $word.Documents.Open($docxPath)
    
    $totalPages = $doc.ComputeStatistics(2)
    Write-Host "Total Pages in Final Document: $totalPages"
    
    $targetPaths = @(
        "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Based_Yoga_Trainer_Project_Report_Final.pdf",
        "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI-Based-Yoga-Trainer-Project-Report.pdf"
    )
    
    foreach ($p in $targetPaths) {
        try {
            Write-Host "Attempting export to: $p"
            if (Test-Path $p) {
                Remove-Item $p -Force -ErrorAction SilentlyContinue
            }
            $doc.ExportAsFixedFormat($p, 17, $false, 0, 0, 1, $totalPages, 0, $true, $true, 0, $true, $true, $false)
            Write-Host "SUCCESS: Exported to $p"
        } catch {
            Write-Host "Notice: Could not write to $p (file may be locked by viewer): $($_.Exception.Message)"
        }
    }
    
    $doc.Close([ref]0)
} finally {
    $word.Quit()
}
