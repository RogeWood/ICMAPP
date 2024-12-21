using System.Diagnostics;
using System.IO;
using UnityEngine;

public class PythonCodeIOManager : MonoBehaviour
{
	public string pythonPath = "python"; // Python �i�����ɪ����|
	public string scriptPath = "path/to/save_image.py"; // Python �}�������|
	public Renderer targetRenderer; // �Ω���ܹϤ��� Renderer (�Ҧp Quad �W������)

	void Start()
	{
		string imagePath = RunPythonScriptAndGetImagePath();
		if (!string.IsNullOrEmpty(imagePath) && File.Exists(imagePath))
		{
			LoadImageToTexture(imagePath);
		}
		else
		{
			UnityEngine.Debug.LogError("Image file not found: " + imagePath);
		}
	}

	string RunPythonScriptAndGetImagePath()
	{
		ProcessStartInfo start = new ProcessStartInfo();
		start.FileName = pythonPath;
		start.Arguments = scriptPath;
		start.UseShellExecute = false;
		start.RedirectStandardOutput = true;
		start.RedirectStandardError = true;
		start.CreateNoWindow = true;

		using (Process process = Process.Start(start))
		{
			using (StreamReader reader = process.StandardOutput)
			{
				string output = reader.ReadToEnd().Trim();
				UnityEngine.Debug.Log("Python Output: " + output);
				return output; // ��^ Python ��X���Ϥ����|
			}
		}
	}

	void LoadImageToTexture(string imagePath)
	{
		byte[] imageData = File.ReadAllBytes(imagePath);
		Texture2D texture = new Texture2D(2, 2);
		texture.LoadImage(imageData);

		// �N�Ϥ����Ψ���w������
		if (targetRenderer != null)
		{
			targetRenderer.material.mainTexture = texture;
		}
	}
}