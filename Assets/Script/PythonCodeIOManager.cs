using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using static System.Net.WebRequestMethods;
using TMPro;
using System;
using UnityEngine.UI;

public class PythonCodeIOManager : MonoBehaviour
{
	//[SerializeField] private string pythonPath = "C:\\Users\\user\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe"; // Python 可執行檔的路徑
	[SerializeField] private string scriptPath = "path/to/save_image.py"; // Python 腳本的路徑
	[SerializeField] private string pythonServerUrl = "http://localhost:5000/";
	[SerializeField] private TextMeshProUGUI severStatus;
	//"http://localhost:5000/run_python_code"
	//http://localhost:5000/code1_kappa?input_string=hello

	//[SerializeField] private string outputTxtPath = "Assets/pythonCode/output.txt";
	//[SerializeField] private string inputTxtPath = "Assets/pythonCode/input.txt";

	public string outputString;

	void Start()
	{
		StartCoroutine(TestPythonServer());
	}

	IEnumerator TestPythonServer()
	{
		using (UnityWebRequest webRequest = UnityWebRequest.Get(pythonServerUrl + "/run_python_code"))
		{
			// Send the request and wait for a response
			yield return webRequest.SendWebRequest();

			if (webRequest.result == UnityWebRequest.Result.Success)
			{
				// Successfully received response from Python server
				Debug.Log("Received from Python: " + webRequest.downloadHandler.text);
				//outputString = webRequest.downloadHandler.text;
				severStatus.text = "python server status: \n" + webRequest.downloadHandler.text + "\n" + pythonServerUrl;
			}
			else
			{
				// Error occurred
				Debug.LogError("Error: " + webRequest.error);
			}
		}
	}

	public IEnumerator GetPythonData(string api, string inputString, TextMeshProUGUI tmp)
	{
		string url = pythonServerUrl + api + "?input_string=" + inputString;
		Debug.Log(url);
		using (UnityWebRequest webRequest = UnityWebRequest.Get(url))
		{
			// Send the request and wait for a response
			yield return webRequest.SendWebRequest();

			if (webRequest.result == UnityWebRequest.Result.Success)
			{
				// Successfully received response from Python server
				Debug.Log("Received from Python: " + webRequest.downloadHandler.text);
				outputString = webRequest.downloadHandler.text;
				tmp.text = "Output:  " + outputString;
			}
			else
			{
				// Error occurred
				Debug.LogError("Error: " + webRequest.error);
			}
		}
	}

	public IEnumerator GetPythonImage(string api, string inputString, Image uiImage)
	{
		string url = pythonServerUrl + api + "?input_string=" + inputString;
		Debug.Log(url);
		using (UnityWebRequest request = UnityWebRequestTexture.GetTexture(url))
		{
			yield return request.SendWebRequest();

			if (request.result != UnityWebRequest.Result.Success)
			{
				Debug.LogError("Error: " + request.error);
			}
			else
			{
				Texture2D texture = ((DownloadHandlerTexture)request.downloadHandler).texture;

				// Create a Sprite from the Texture2D
				Rect rect = new Rect(0, 0, texture.width, texture.height);
				Vector2 pivot = new Vector2(0.5f, 0.5f); // Center pivot
				Sprite sprite = Sprite.Create(texture, rect, pivot);

				// Assign the Sprite to the UI Image component
				uiImage.sprite = sprite;
			}
		}
	}

}
