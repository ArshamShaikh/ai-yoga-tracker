$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Complete.docx"
    $doc = $word.Documents.Open($docPath)
    $pages = $doc.ComputeStatistics(2) # wdStatisticPages = 2
    Write-Host "Total Pages in Doc: $pages"
    $doc.Close([ref]0)
} finally {
    $word.Quit()
}
