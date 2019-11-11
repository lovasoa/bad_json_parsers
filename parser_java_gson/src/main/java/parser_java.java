import com.google.gson.*;
import java.io.InputStreamReader;

class Parser_Java {
  public static void main(String[] args) throws java.io.IOException {
    JsonElement result = new JsonParser().parse(new InputStreamReader(System.in));
    assert result != null;
  }
}
