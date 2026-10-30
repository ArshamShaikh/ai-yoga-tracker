$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docPath = "c:\arsham\TY\MP\ai-yoga-tracker\scripts\test_restart_proper.docx"
    $doc = $word.Documents.Open($docPath)
    $sec2 = $doc.Sections.Item(2)
    # Check page number of Chapter 1
    $firstP = $sec2.Range.Paragraphs.Item(1)
    $pNum = $firstP.Range.Information(3) # wdActiveEndAdjustedPageNumber
    Write-Host "Adjusted Page Number of Chapter 1: $pNum"
    $rawNum = $firstP.Range.Information(1) # wdActiveEndPageNumber
    Write-Host "Raw Page Number of Chapter 1: $rawNum"
    
    $doc.Close([ref]0)
} finally {
    $word.Quit()
}
