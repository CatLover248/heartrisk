namespace heartrisk;
using System.Text;
public partial class MainPage : ContentPage
{
	private readonly HttpClient httpClient = new HttpClient();
	private string defaultUrl = "http://127.0.0.1:5000/predict";

	public MainPage()
	{
		InitializeComponent();
	}

    private async void SendRequestBtn_Clicked(object sender, EventArgs e)
    {
		string jsonData = "{\"Age\":\"" + Age.Text + "\",\"Sex\":\"" + Sex.Text + "\",\"Cholesterol\":\"" + Cholesterol.Text + "\",\"Diastolic\":\"" + Diastolic.Text + "\",\"Systolic\":\"" + Systolic.Text + "\",\"Heart_Rate\":\"" + Heart_Rate.Text + "\",\"Diabetes\":\"" + Diabetes.Text + "\",\"Family_History\":\"" + Family_History.Text + "\",\"Smoking\":\"" + Smoking.Text + "\",\"Obesity\":\"" + Obesity.Text + "\",\"Alcohol_Consumption\":\"" + Alcohol_Consumption.Text + "\",\"Exercise_Hours_Per_Week\":\"" + Exercise_Hours_Per_Week.Text + "\",\"Diet\":\"" + Diet.Text + "\",\"Previous_Heart_Problems\":\"" + Previous_Heart_Problems.Text + "\",\"Medication_Use\":\"" + Medication_Use.Text + "\",\"Stress_Level\":\"" + Stress_Level.Text + "\",\"Sedentary_Hours_Per_Day\":\"" + Sedentary_Hours_Per_Day.Text + "\",\"Income\":\"" + Income.Text + "\",\"BMI\":\"" + BMI.Text + "\",\"Triglycerides\":\"" + Triglycerides.Text + "\",\"Physical_Activity_Days_Per_Week\":\"" + Physical_Activity_Days_Per_Week.Text + "\",\"Sleep_Hours_Per_Day\":\"" + Sleep_Hours_Per_Day.Text + "\"}";
		var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
		Console.WriteLine(jsonData);
		if(UrlLabel.Text.Trim() == "default")
		{
			UrlLabel.Text = defaultUrl;
		}
		var response = await this.httpClient.PostAsync(UrlLabel.Text,content);
		if(response.IsSuccessStatusCode)
		{
			string responseContent = await response.Content.ReadAsStringAsync();
			ResponseLabel.Text = responseContent;

        } else
		{
			ResponseLabel.Text = response.StatusCode.ToString();

        }
    }
}

