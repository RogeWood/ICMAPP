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

    public void OnClickNextPage()
    {
        UpdatePages(currentPageIndex+1);
    }

    private void UpdatePages(int pageIndex)
    {
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
        currentPageIndex = pageIndex;
    }

	public void OnClickEnterKappa()
    {
        string inputValue = kappaInputField.text;
        Debug.Log(inputValue);
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

    public void OnClickExit()
    {
		Application.Quit();
	}
}
