import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

public class FirstUniqueChar {
    public static void main(String[] args){

    }
    public int firstUniqChar(String s) {
        if(s.length() == 0)
            return -1;
        if(s.length() ==1)
            return 0;
        LinkedHashSet<Character> uniqueSet = new LinkedHashSet<>();

        Set<Character> seen = new HashSet<>();
        for(char c: s.toCharArray()){
            if(seen.contains(c)){
                uniqueSet.remove(c);
            }
            else{
                seen.add(c);
                uniqueSet.add(c);
            }
        }
        if(!uniqueSet.isEmpty())
            return s.indexOf(uniqueSet.iterator().next());
        return -1;
    }
}
