import java.net.http.*;
import java.net.URI;


public class NetworkCalls
{
    public static void main(String[] args) throws Exception{
        System.out.println("Namaskara");
        makeAHTTPRequestPrintResponse();
    }

    public static void makeAHTTPRequestPrintResponse() throws Exception
    {
        HttpClient client = HttpClient.newBuilder().build();
        HttpRequest req = HttpRequest.newBuilder(
        URI.create("https://jsonplaceholder.typicode.com/posts/1")).build();
        HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status: " + resp.statusCode());
        System.out.println("Headers: " + resp.headers());
        System.out.println("Body: " + resp.body().substring(0, 120));


    }
}