$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Complete.docx"
    $doc = $word.Documents.Open($docPath)
    Write-Host "Total Paragraphs: $($doc.Paragraphs.Count)"
    
    # Check first few headings
    $count = 0
    foreach ($p in $doc.Paragraphs) {
        $txt = $p.Range.Text.Trim()
        if ($txt -match "^CHAPTER \d" -or $txt -match "^\d\.\d") {
            $page = $p.Range.Information(3) # 3 = wdActiveEndAdjustedPageNumber
            Write-Host "$txt --> Page $page"
            $count++
            if ($count -ge 15) { break }
        }
    }
    $doc.Close([ref]0)
} finally {
    $word.Quit()
}
