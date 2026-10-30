$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docPath = "c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx"
    $doc = $word.Documents.Open($docPath)
    Write-Host "Total Pages: $($doc.ComputeStatistics(2))"
    
    # We want to find each heading in Section 2 (the chapters section)
    # The TOC is in Section 1. Section 2 begins at Chapter 1.
    $sec2 = $doc.Sections.Item(2)
    Write-Host "Section 2 starts at character position: $($sec2.Range.Start)"
    
    $results = @()
    foreach ($p in $sec2.Range.Paragraphs) {
        $txt = $p.Range.Text.Trim()
        # Look for Chapter or numbered section headings
        if ($txt -match "^CHAPTER \d\." -or $txt -match "^\d\.\d(\.\d)?(\.\d)?\s+") {
            # Clean text
            $cleanTitle = $txt.Split([char]13)[0].Split([char]10)[0].Trim()
            $pageNum = $p.Range.Information(1) # 1 = wdActiveEndAdjustedPageNumber (page number displayed in Section 2, starting at 1)
            $results += "$cleanTitle|||$pageNum"
        }
    }
    
    $resultsPath = "c:\arsham\TY\MP\ai-yoga-tracker\scripts\heading_pages.txt"
    $results | Out-File -FilePath $resultsPath -Encoding UTF8
    Write-Host "Extracted $($results.Count) headings to $resultsPath"
    
    $doc.Close([ref]0)
} finally {
    $word.Quit()
}
