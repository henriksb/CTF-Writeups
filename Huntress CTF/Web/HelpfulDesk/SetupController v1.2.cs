public class SetupController : Controller
{
	private readonly string _credsFilePath = "credentials.json";

	public IActionResult SetupWizard()
	{
		if (System.IO.File.Exists(_credsFilePath))
		{
			string requestPath = base.HttpContext.Request.Path.Value.TrimEnd('/');
			if (requestPath.Equals("/Setup/SetupWizard", StringComparison.OrdinalIgnoreCase))
			{
				return View("Error", new ErrorViewModel
				{
					RequestId = "Server already set up.",
					ExceptionMessage = "Server already set up.",
					StatusCode = 403
				});
			}
		}
		return View();
	}

	[HttpPost]
	public IActionResult SetupWizard(string username, string password)
	{
		string filePath = Path.Combine(Directory.GetCurrentDirectory(), "credentials.json");
		List<AuthenticationService.UserCredentials> credentials = new List<AuthenticationService.UserCredentials>
		{
			new AuthenticationService.UserCredentials
			{
				Username = username,
				Password = password,
				IsAdmin = true
			}
		};
		string json = JsonSerializer.Serialize(credentials);
		System.IO.File.WriteAllText(filePath, json);
		return RedirectToAction("SetupComplete");
	}

	public IActionResult SetupComplete()
	{
		return View();
	}
}
