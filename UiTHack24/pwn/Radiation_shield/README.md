# Radiation Shield
Deep within the space station "Pandora", a looming solar flare threatens the lives of the station's crew. The crew is locked out of the radiation shield controls, so you must hack into the system to increase the shield's protection to maximum.

## Filer
shield.c\
shield\
libc.so.6

## Løsning
I denne oppgaven skal vi utnytte en "buffer overflow". I C-filen kan vi se den viktige delen av koden:

```c
void shield_control(){
    char shield_level[10] = "medium";
    char shield_status[10] = {0};

    printf("New shield status:\n");
    fgets(shield_status, 20, stdin);

    printf("Shield status: %s\n", shield_status);
    printf("Shield level: %s\n", shield_level);

    if(strncmp(shield_level, "maximum", 7) == 0){
        print_flag();
    }
}

int main(){
    ignore_me();
    ignore_me_timeout();

    shield_control();
    return 0;
}
```
Problemet her er at vi ikke kan endre på variabelen `shield_level`, som betyr at vi aldri kan nå `print_flag();`.

For å skrive over variabelen må vi overskrive 10 bytes, da dette er den allokerte størrelsen på variabelen. Skriver man `0000000000maximum` (10 nuller) blir den overskrevet.

`UiTHack24{M4ximum_sh13ld_0verflooow}`
