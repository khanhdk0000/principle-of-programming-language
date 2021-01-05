.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
	iconst_4
	putstatic BKITClass/a I
	iconst_5
	putstatic BKITClass/b I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is t Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic BKITClass/f(Z)V
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic BKITClass/f(Z)V
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic BKITClass/f(Z)V
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic BKITClass/f(Z)V
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic BKITClass/f(Z)V
	getstatic BKITClass/a I
	getstatic BKITClass/b I
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic BKITClass/f(Z)V
Label1:
	return
.limit stack 14
.limit locals 2
.end method

.method public static f(Z)V
.var 0 is x Z from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
.limit locals 1
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
