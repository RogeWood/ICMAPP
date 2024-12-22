//using System.Collections;
//using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class MenuButtonController : MonoBehaviour
{
	[Header("variable")]
	[SerializeField] private int currentPageIndex = 0;


	[Header("panel")]
	[SerializeField] private GameObject pagePanel;
    [SerializeField] private GameObject[] pages;


	[Header("input field")]
	[SerializeField] private TMP_InputField kappaInputField;
	[SerializeField] private TMP_InputField qrfactorInputField;
	[SerializeField] private TMP_InputField minimizeInputField1;
	[SerializeField] private TMP_InputField minimizeInputField2;
	[SerializeField] private TMP_InputField fixedIterationInputField;
	[SerializeField] private TMP_InputField fixedSolveInputField;
	[SerializeField] private TMP_InputField secentMethodInputField1;
	[SerializeField] private TMP_InputField secentMethodInputField2;


	[Header("TMP")]
	[SerializeField] private TextMeshProUGUI kappaOutTMP;
	[SerializeField] private TextMeshProUGUI qrfactorOutTMP;
	[SerializeField] private TextMeshProUGUI minimizeOutTMP;
	[SerializeField] private TextMeshProUGUI fixedSolveOutTMP;
	[SerializeField] private TextMeshProUGUI secentMethodOutTMP;
	
	[Header("script")]
    [SerializeField] private PythonCodeIOManager pythonCodeIOManager;

	[Header("image")]
	[SerializeField] private Image fixedIterationOutImage;
	//[SerializeField] private PythonCodeIOManager pythonCodeIOManager;
	// Start is called before the first frame update
	void Start()
    {
        currentPageIndex = 0;
        pagePanel.SetActive(false);
	}

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnClickChapter(GameObject page = null)
    {
        pagePanel.SetActive(true);

        if(page)
        {
            int index = GetIndexFromName(page.gameObject.name);
            Debug.Log(index);
            UpdatePages(index);
		}
    }
    

    public void OnClickBackToMenu()
    {
        pagePanel.SetActive(false);
    }

    public void OnClickNextPage(int i)
    {
        UpdatePages(currentPageIndex + i);
    }

    private void UpdatePages(int pageIndex)
    {
		if (pageIndex >= pages.Length || pageIndex < 0) return;
        currentPageIndex = pageIndex;


        foreach (var page in pages)
        {
            if(page) page.SetActive(false);
            else
            {
                //Debug.Log("no pages!!!!!!!!   end index: " + page.gameObject.name);
				return; // not found page
			}
        }

        pages[pageIndex].SetActive(true);
    }

	public void OnClickEnterKappa()
    {
        StartCoroutine(pythonCodeIOManager.GetPythonData("kappa", kappaInputField.text, kappaOutTMP));

	}

	public void OnClickEnterQRfactor()
	{
        StartCoroutine(pythonCodeIOManager.GetPythonData("qrfactor", qrfactorInputField.text, qrfactorOutTMP));
	}
	public void OnClickEnterMinimize()
	{
		string inputValue = minimizeInputField1.text + "|" + minimizeInputField2.text;
		StartCoroutine(pythonCodeIOManager.GetPythonData("minimize", inputValue, minimizeOutTMP));
	}

	public void OnClickEnterFixedSolve()
	{
		StartCoroutine(pythonCodeIOManager.GetPythonData("fixedSolve", fixedSolveInputField.text, fixedSolveOutTMP));
	}

	public void OnClickEnterFixedIteration()
	{
		StartCoroutine(pythonCodeIOManager.GetPythonImage("fixedIteration", fixedIterationInputField.text, fixedIterationOutImage));
	}

	public void OnClickEnterSecentMethod()
	{

		string inputValue = secentMethodInputField1.text + "|" + secentMethodInputField2.text;
		StartCoroutine(pythonCodeIOManager.GetPythonData("secentMethod", inputValue, secentMethodOutTMP));
	}

	

	public void OnClickExit()
    {
		Application.Quit();
	}

    private int GetIndexFromName(string name)
	{
		int startIndex = name.IndexOf('(');
		int endIndex = name.IndexOf(')');

		if (startIndex != -1 && endIndex != -1 && endIndex > startIndex)
		{
			string indexString = name.Substring(startIndex + 1, endIndex - startIndex - 1);
			if (int.TryParse(indexString, out int index))
			{
				return index-1;
			}
		}

		return -1;
	}
}
