using System.Diagnostics;
using System.IO;
using UnityEngine;

public class PythonCodeIOManager : MonoBehaviour
{
	public string pythonPath = "python"; // Python 可執行檔的路徑
	public string scriptPath = "path/to/save_image.py"; // Python 腳本的路徑
	public Renderer targetRenderer; // 用於顯示圖片的 Renderer (例如 Quad 上的材質)

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
				return output; // 返回 Python 輸出的圖片路徑
			}
		}
	}

	void LoadImageToTexture(string imagePath)
	{
		byte[] imageData = File.ReadAllBytes(imagePath);
		Texture2D texture = new Texture2D(2, 2);
		texture.LoadImage(imageData);

		// 將圖片應用到指定的材質
		if (targetRenderer != null)
		{
			targetRenderer.material.mainTexture = texture;
		}
	}
}
