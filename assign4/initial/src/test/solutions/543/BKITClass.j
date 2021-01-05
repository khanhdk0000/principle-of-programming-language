.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
	iconst_1
	putstatic BKITClass/a I
	iconst_2
	putstatic BKITClass/b I
	iconst_3
	putstatic BKITClass/c I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 15
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 2 is i I from Label7 to Label8
.var 3 is j I from Label7 to Label8
	iconst_0
	istore_2
	iconst_0
	istore_3
	getstatic BKITClass/b I
	iload_1
	iadd
	istore_2
	getstatic BKITClass/c I
	iload_1
	iadd
	istore_3
	iload_2
	iload_3
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
