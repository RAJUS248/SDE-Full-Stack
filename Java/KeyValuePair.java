
public class KeyValuePair <K, V> {

    private K key;
    private V value;

    public KeyValuePair (K key, V value)
    {
        this.key = key;
        this.value = value;
    }

    public void PrintValues()
    {
        System.out.println("Key is " + this.key + " Value is = " + this.value);
    }
    
    
}
