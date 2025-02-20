import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class TestMap {
    public static void main(String[] args) {

        Map<Integer, String> map = new HashMap<>();
        map.put(1, "value1");
        map.put(2, "value2");
        map.put(3, "value3");
        map.put(4, "value4");

        System.out.println(map.get(1));
    }
}
